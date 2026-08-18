# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 350
- HTTP: 403 alive / 50 gold
- HTTPS: 214 alive / 14 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 243 alive / 144 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14856
- Ever gold: 475

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
