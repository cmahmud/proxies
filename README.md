# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 384
- HTTP: 180 alive / 80 gold
- HTTPS: 146 alive / 20 gold
- SOCKS4: 218 alive / 144 gold
- SOCKS5: 199 alive / 140 gold

## Historical pool

- Discovered: 149512
- Ever alive: 26910
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
