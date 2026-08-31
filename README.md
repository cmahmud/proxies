# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 453
- HTTP: 167 alive / 88 gold
- HTTPS: 100 alive / 29 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 238 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45344
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
