# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 400
- HTTP: 112 alive / 65 gold
- HTTPS: 167 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40954
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
