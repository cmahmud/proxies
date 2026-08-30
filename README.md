# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 440
- HTTP: 114 alive / 77 gold
- HTTPS: 116 alive / 33 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44636
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
