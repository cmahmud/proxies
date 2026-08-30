# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 445
- HTTP: 128 alive / 89 gold
- HTTPS: 77 alive / 35 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 200 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44270
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
