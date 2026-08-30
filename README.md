# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 446
- HTTP: 112 alive / 81 gold
- HTTPS: 64 alive / 32 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 207 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44587
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
