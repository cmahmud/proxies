# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 443
- HTTP: 123 alive / 79 gold
- HTTPS: 65 alive / 30 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45558
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
