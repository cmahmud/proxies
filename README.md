# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 413
- HTTP: 115 alive / 69 gold
- HTTPS: 165 alive / 15 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41168
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
