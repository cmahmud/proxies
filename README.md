# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 411
- HTTP: 144 alive / 73 gold
- HTTPS: 153 alive / 20 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40253
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
