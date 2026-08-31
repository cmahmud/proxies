# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 479
- HTTP: 136 alive / 100 gold
- HTTPS: 123 alive / 44 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45035
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
