# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 463
- HTTP: 128 alive / 95 gold
- HTTPS: 54 alive / 32 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49410
- Ever gold: 1580

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
