# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 420
- HTTP: 105 alive / 61 gold
- HTTPS: 102 alive / 24 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35845
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
