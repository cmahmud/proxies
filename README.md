# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 494
- HTTP: 145 alive / 103 gold
- HTTPS: 141 alive / 52 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45006
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
