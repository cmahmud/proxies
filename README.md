# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 445
- HTTP: 128 alive / 76 gold
- HTTPS: 109 alive / 33 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 220 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45379
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
