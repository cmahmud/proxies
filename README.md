# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 427
- HTTP: 350 alive / 91 gold
- HTTPS: 200 alive / 26 gold
- SOCKS4: 210 alive / 151 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30091
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
