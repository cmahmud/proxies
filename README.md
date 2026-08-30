# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 418
- HTTP: 112 alive / 77 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44484
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
