# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 491
- HTTP: 151 alive / 105 gold
- HTTPS: 127 alive / 45 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 196 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44954
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
