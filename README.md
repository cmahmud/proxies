# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 453
- HTTP: 128 alive / 83 gold
- HTTPS: 90 alive / 36 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 220 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45354
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
