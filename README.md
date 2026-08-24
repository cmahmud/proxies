# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 384
- HTTP: 126 alive / 70 gold
- HTTPS: 96 alive / 14 gold
- SOCKS4: 164 alive / 149 gold
- SOCKS5: 186 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33234
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
