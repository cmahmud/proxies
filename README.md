# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 453
- HTTP: 145 alive / 84 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 224 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45360
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
