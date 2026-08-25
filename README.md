# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 424
- HTTP: 106 alive / 65 gold
- HTTPS: 83 alive / 23 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35967
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
