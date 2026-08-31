# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 484
- HTTP: 150 alive / 97 gold
- HTTPS: 127 alive / 49 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45022
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
