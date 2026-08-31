# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 481
- HTTP: 141 alive / 98 gold
- HTTPS: 113 alive / 44 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45101
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
