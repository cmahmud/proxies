# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 402
- HTTP: 109 alive / 69 gold
- HTTPS: 101 alive / 11 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33307
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
