# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 441
- HTTP: 142 alive / 76 gold
- HTTPS: 106 alive / 33 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 204 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45373
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
