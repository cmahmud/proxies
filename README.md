# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 306
- HTTP: 161 alive / 77 gold
- HTTPS: 30 alive / 16 gold
- SOCKS4: 82 alive / 73 gold
- SOCKS5: 173 alive / 140 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47820
- Ever gold: 1494

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
