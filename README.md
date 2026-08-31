# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 483
- HTTP: 149 alive / 97 gold
- HTTPS: 130 alive / 48 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45022
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
