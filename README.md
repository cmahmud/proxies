# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 400
- HTTP: 85 alive / 57 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42849
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
