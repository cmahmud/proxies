# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 424
- HTTP: 106 alive / 64 gold
- HTTPS: 79 alive / 24 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35957
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
