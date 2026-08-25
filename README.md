# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 414
- HTTP: 93 alive / 57 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36157
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
