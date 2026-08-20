# SyndProxy private pool

## Current pool

- Alive now: 1898
- Gold now: 693
- HTTP: 729 alive / 234 gold
- HTTPS: 628 alive / 149 gold
- SOCKS4: 221 alive / 147 gold
- SOCKS5: 320 alive / 163 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24479
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
