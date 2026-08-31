# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 439
- HTTP: 134 alive / 72 gold
- HTTPS: 109 alive / 32 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 214 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45373
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
