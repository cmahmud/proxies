# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 93 alive / 57 gold
- HTTPS: 84 alive / 18 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36164
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
