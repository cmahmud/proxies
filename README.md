# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 486
- HTTP: 150 alive / 98 gold
- HTTPS: 125 alive / 50 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45025
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
