# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 453
- HTTP: 144 alive / 84 gold
- HTTPS: 101 alive / 32 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 222 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45361
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
