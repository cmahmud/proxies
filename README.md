# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 427
- HTTP: 164 alive / 76 gold
- HTTPS: 74 alive / 23 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33877
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
