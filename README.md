# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 476
- HTTP: 144 alive / 100 gold
- HTTPS: 125 alive / 40 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45053
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
