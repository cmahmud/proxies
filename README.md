# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 427
- HTTP: 105 alive / 70 gold
- HTTPS: 90 alive / 26 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35716
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
