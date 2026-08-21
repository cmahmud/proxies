# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 451
- HTTP: 364 alive / 111 gold
- HTTPS: 234 alive / 34 gold
- SOCKS4: 205 alive / 154 gold
- SOCKS5: 245 alive / 152 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28604
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
