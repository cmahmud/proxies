# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 410
- HTTP: 146 alive / 73 gold
- HTTPS: 156 alive / 20 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40257
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
