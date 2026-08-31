# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 484
- HTTP: 157 alive / 97 gold
- HTTPS: 124 alive / 50 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45025
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
