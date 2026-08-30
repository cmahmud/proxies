# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 476
- HTTP: 137 alive / 96 gold
- HTTPS: 121 alive / 43 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44871
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
