# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 422
- HTTP: 133 alive / 65 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 211 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45526
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
