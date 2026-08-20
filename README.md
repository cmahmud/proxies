# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 374
- HTTP: 192 alive / 69 gold
- HTTPS: 145 alive / 20 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 211 alive / 138 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26155
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
