# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 490
- HTTP: 149 alive / 104 gold
- HTTPS: 128 alive / 46 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44957
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
