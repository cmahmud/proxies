# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 425
- HTTP: 127 alive / 83 gold
- HTTPS: 61 alive / 28 gold
- SOCKS4: 155 alive / 151 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
