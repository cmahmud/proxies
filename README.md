# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 386
- HTTP: 122 alive / 49 gold
- HTTPS: 56 alive / 12 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33582
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
