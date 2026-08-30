# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 479
- HTTP: 148 alive / 99 gold
- HTTPS: 123 alive / 43 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44946
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
