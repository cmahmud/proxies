# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 457
- HTTP: 125 alive / 85 gold
- HTTPS: 123 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46753
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
