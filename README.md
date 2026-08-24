# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 389
- HTTP: 113 alive / 73 gold
- HTTPS: 65 alive / 14 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 187 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33239
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
