# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 450
- HTTP: 133 alive / 81 gold
- HTTPS: 100 alive / 33 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 216 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45362
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
