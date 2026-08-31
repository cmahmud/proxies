# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 451
- HTTP: 126 alive / 79 gold
- HTTPS: 122 alive / 36 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45628
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
