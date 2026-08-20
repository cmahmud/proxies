# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 384
- HTTP: 199 alive / 78 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 197 alive / 141 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26630
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
